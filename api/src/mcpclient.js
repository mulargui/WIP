import { LambdaClient, GetFunctionUrlConfigCommand } from "@aws-sdk/client-lambda";
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import { z } from 'zod/v3';
import * as fs from 'fs'; 
import * as path from 'path';
import { fileURLToPath } from 'url';

export default class MCPClient {

  constructor() {}
  async createInstance() {    
    try {
      // Read the config file
      const __filename = fileURLToPath(import.meta.url);
      const __dirname = path.dirname(__filename);
      const configPath = path.join(__dirname, 'config.json');
      const rawConfig = fs.readFileSync(configPath);
      const config = JSON.parse(rawConfig);

      this.REGION = process.env.AWS_REGION || "us-east-1";

      //get the url of the MCP server
      const mcpFunctionName = config.mcp.functionName;
      let mcpServerUrl = await this.getLambdaFunctionUrl(mcpFunctionName);
      mcpServerUrl += "mcp";
      console.log(`URL of the MCP Server: ${mcpServerUrl}`);

      // connect to the MCP Server
      this.client = new Client({
        name: 'healthylinkx-mcp-client',
        version: '1.0.0',
        title: 'Healthylinkx Chat Client Application'
      });
      const httpTransport = new StreamableHTTPClientTransport(mcpServerUrl);
      await this.client.connect(httpTransport);
    }catch(error){
      console.error("MCP Server constructor error: ", error);
      throw error;
    }
  }

  // helper function to get the URL of the MCP Server
  async getLambdaFunctionUrl(functionName) {
    const client = new LambdaClient({ region: this.REGION });
    const command = new GetFunctionUrlConfigCommand({
      FunctionName: functionName,
    });
    const response = await client.send(command);
    return response.FunctionUrl;
  }

  //Get the list of tools available at the MCP Server
  async GetTools() {

    try {
      const tools = await this.client.listTools();
      console.log('MCP Server available tools:', tools);
      return tools;
    } catch (error) {
      console.error("Failed to retrieve MCP tools: ", error);
      throw error;
    }
  }
    // Example: Calling a tool (assuming a tool named 'add' exists)
    //const result = await client.callTool('add', { a: 5, b: 3 });
    //console.log('Addition result:', result);
}
