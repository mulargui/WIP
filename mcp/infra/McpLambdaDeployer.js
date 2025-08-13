/**
 * @fileoverview MCP Lambda deployment module for the Bedrock demo app.
 * This module provides a class for deploying and updating MCP Lambda functions.
 * @module McpLambdaDeployer
 */

const { 
  LambdaClient, 
  CreateFunctionCommand, 
  UpdateFunctionCodeCommand,
  CreateFunctionUrlConfigCommand,
  UpdateFunctionUrlConfigCommand,
  GetFunctionUrlConfigCommand,
  AddPermissionCommand
} = require("@aws-sdk/client-lambda");
const { IAMClient, GetRoleCommand, CreateRoleCommand, AttachRolePolicyCommand } = require("@aws-sdk/client-iam");
const AdmZip = require("adm-zip");
const fs = require("fs");
const path = require('path');
const util = require('util');
const writeFileAsync = util.promisify(fs.writeFile);

class McpLambdaDeployer {
  constructor() {
    const configPath = path.join(__dirname, '..', 'config.json');
    const rawConfig = fs.readFileSync(configPath);
    this.config = JSON.parse(rawConfig);
    this.FUNCTION_NAME = this.config.mcp.functionName;
    this.ROLE_NAME = this.config.mcp.roleName;
    this.REGION = process.env.AWS_REGION || "us-east-1";
  }

  async createLambdaRole() {
    const rolePolicy = {
      Version: "2012-10-17",
      Statement: [
        {
          Effect: "Allow",
          Principal: {
            Service: "lambda.amazonaws.com"
          },
          Action: "sts:AssumeRole"
        }
      ]
    };
    const iam = new IAMClient({ region: this.REGION });
    try {
      const getRoleCommand = new GetRoleCommand({ RoleName: this.ROLE_NAME });
      const { Role } = await iam.send(getRoleCommand);
      return Role.Arn;
    } catch (error) {
      if (error.name === "NoSuchEntityException") {
        const createRoleCommand = new CreateRoleCommand({
          RoleName: this.ROLE_NAME,
          AssumeRolePolicyDocument: JSON.stringify(rolePolicy)
        });
        const { Role } = await iam.send(createRoleCommand);
        await this.attachPolicies(this.ROLE_NAME);
        await new Promise(resolve => setTimeout(resolve, 10000));
        return Role.Arn;
      } else {
        throw error;
      }
    }
  }

  async attachPolicies(roleName) {
    const iam = new IAMClient({ region: this.REGION });
    const policies = [
      "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
      "arn:aws:iam::aws:policy/AmazonRDSFullAccess"
    ];
    for (const policyArn of policies) {
      await iam.send(new AttachRolePolicyCommand({
        RoleName: roleName,
        PolicyArn: policyArn
      }));
    }
  }


  /**
   * Creates or updates the function URL for the Lambda.
   * @param {string} functionName - The name of the Lambda function.
   * @returns {Promise<void>}
   * @throws {Error} If function URL creation or update fails.
   */
  async createFunctionUrl(functionName) {
    const lambda = new LambdaClient({ region: this.REGION });
    try {
      // Check if function URL already exists
      const getFunctionUrlCommand = new GetFunctionUrlConfigCommand({ FunctionName: functionName });
      await lambda.send(getFunctionUrlCommand);
      
      // If it exists, update it
      const updateFunctionUrlCommand = new UpdateFunctionUrlConfigCommand({
        FunctionName: functionName,
        AuthType: "NONE",
        Cors: {
          AllowCredentials: true,
          AllowHeaders: ["*"],
          AllowMethods: ["*"],
          AllowOrigins: ["*"],
          ExposeHeaders: ["*"],
          MaxAge: 86400
        }
      });
      const response = await lambda.send(updateFunctionUrlCommand);
      console.log("MCP Function URL updated:", response.FunctionUrl);
    } catch (error) {
      if (error.name === "ResourceNotFoundException") {
        // If it doesn't exist, create it
        const createFunctionUrlCommand = new CreateFunctionUrlConfigCommand({
          FunctionName: functionName,
          AuthType: "NONE",
          Cors: {
            AllowCredentials: true,
            AllowHeaders: ["*"],
            AllowMethods: ["*"],
            AllowOrigins: ["*"],
            ExposeHeaders: ["*"],
            MaxAge: 86400
          }
        });
        const response = await lambda.send(createFunctionUrlCommand);
        console.log("MCP Function URL created:", response.FunctionUrl);
      } else {
        throw error;
      }
    }

    // Add permission for public access
    await this.addFunctionUrlPermission(functionName);
  }

  /**
   * Adds permission for public access to the function URL.
   * @param {string} functionName - The name of the Lambda function.
   * @returns {Promise<void>}
   * @throws {Error} If adding permission fails.
   */
  async addFunctionUrlPermission(functionName) {
    try {
      const lambda = new LambdaClient({ region: this.REGION });
      const addPermissionCommand = new AddPermissionCommand({
        FunctionName: functionName,
        StatementId: "FunctionURLAllowPublicAccess",
        Action: "lambda:InvokeFunctionUrl",
        Principal: "*",
        FunctionUrlAuthType: "NONE"
      });

      await lambda.send(addPermissionCommand);
      console.log("MCP Function URL public access permission added successfully");
    } catch (error) {
      if (error.name === "ResourceConflictException") {
        console.log("MCP Function URL permission already exists");
      } else {
        throw error;
      }
    }
  }

  /**
   * Saves the function URL to a config file.
   * @param {string} functionName - The name of the Lambda function.
   * @returns {Promise<void>}
   * @throws {Error} If saving the config fails.
   */
  async SaveUrlInConfigFile(functionName) {
    const command = new GetFunctionUrlConfigCommand({ FunctionName: functionName });

    try {
      const lambda = new LambdaClient({ region: this.REGION });
      const response = await lambda.send(command);

      // Save the function URL to lambdaurl.json
      const lambdaurl = { LAMBDA_FUNCTION_URL: response.FunctionUrl };

      await writeFileAsync('mcplambdaurl.json', JSON.stringify(lambdaurl, null, 2));
      console.log(`MCP Lambda url file updated at mcplambdaurl.json`);

    } catch (error) {
      console.error('Error creating and saving MCP Lambda url:', error);
      throw error;
    }
  }

  async deployLambda() {
    const zip = new AdmZip();
    zip.addLocalFile(path.join(__dirname, '../src/mcp_lambda.py'));
    const zipBuffer = zip.toBuffer();
    const roleArn = await this.createLambdaRole();
    const lambda = new LambdaClient({ region: this.REGION });
    try {
      const createFunctionCommand = new CreateFunctionCommand({
        FunctionName: this.FUNCTION_NAME,
        Runtime: "python3.12",
        Role: roleArn,
        Handler: "mcp_lambda.lambda_handler",
        Code: { ZipFile: zipBuffer },
        Timeout: 30,
        MemorySize: 128
      });
      await lambda.send(createFunctionCommand);
      console.log("MCP Lambda function created successfully");
    } catch (error) {
      if (error.name === "ResourceConflictException") {
        console.log("MCP Lambda function already exists. Updating code...");
        const updateFunctionCodeCommand = new UpdateFunctionCodeCommand({
          FunctionName: this.FUNCTION_NAME,
          ZipFile: zipBuffer
        });
        await lambda.send(updateFunctionCodeCommand);
        console.log("MCP Lambda function code updated successfully");
      } else {
        throw error;
      }
    }

    // Create or update function URL
    await this.createFunctionUrl(this.FUNCTION_NAME);
    await this.SaveUrlInConfigFile(this.FUNCTION_NAME);

  }
}

module.exports = McpLambdaDeployer;
