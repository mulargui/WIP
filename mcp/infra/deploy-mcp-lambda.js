const McpLambdaDeployer = require('./McpLambdaDeployer');

async function main() {
  const deployer = new McpLambdaDeployer();
  try {
    await deployer.deployLambda();
  } catch (error) {
    console.error('MCP Lambda deployment failed:', error);
  }
}

main();
