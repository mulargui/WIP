import { LambdaClient, GetFunctionUrlConfigCommand } from "@aws-sdk/client-lambda";
import { McpClient } from '@modelcontextprotocol/sdk/client/mcp.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import { z } from 'zod/v3';
import * as fs from 'fs'; 
import * as path from 'path';
import { fileURLToPath } from 'url';

// Read the config file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const configPath = path.join(__dirname, 'config.json');
const rawConfig = fs.readFileSync(configPath);
const config = JSON.parse(rawConfig);

const mcpFunctionName = config.mcp.functionName;
const REGION = process.env.AWS_REGION || "us-east-1";

// helper function to get the URL of the MCP Server
async function getLambdaFunctionUrl(functionName) {
  const client = new LambdaClient({ region: REGION });

  try {
    const command = new GetFunctionUrlConfigCommand({
      FunctionName: functionName,
    });
    const response = await client.send(command);
    return response.FunctionUrl;
  } catch (error) {
    console.error("Error getting MCP Lambda function URL:", error);
    throw error;
  }
}

export async function MCPGetTools() {

    try {
        //get the url of the MCP Server
        const mcpServerUrl = getLambdaFunctionUrl(mcpFunctionName);
        console.log(`URL of the MCP function: ${mcpServerUrl}`);

        const httpTransport = new StreamableHTTPClientTransport(mcpServerUrl);
        const client = new Client({
            name: 'healthylinkx-mcp-client',
            version: '1.0.0',
            title: 'Healthylinkx Chat Client Application'
        });

        await client.connect(httpTransport);

        // get a list of the tools available at the MCP server
        const tools = await client.listTools();
        console.log('Available tools:', tools);
        return tools;
        
    } catch (err) {
        console.error("Failed to retrieve MCP tools: ", err);
    }

    // Example: Calling a tool (assuming a tool named 'add' exists)
    //const result = await client.callTool('add', { a: 5, b: 3 });
    //console.log('Addition result:', result);
}
