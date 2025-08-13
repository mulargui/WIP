const { 
  LambdaClient, 
  CreateFunctionCommand, 
  UpdateFunctionCodeCommand
} = require("@aws-sdk/client-lambda");
const { IAMClient, GetRoleCommand, CreateRoleCommand, AttachRolePolicyCommand } = require("@aws-sdk/client-iam");
const AdmZip = require("adm-zip");
const fs = require("fs");
const path = require('path');

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
      "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    ];
    for (const policyArn of policies) {
      await iam.send(new AttachRolePolicyCommand({
        RoleName: roleName,
        PolicyArn: policyArn
      }));
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
  }
}

module.exports = McpLambdaDeployer;
