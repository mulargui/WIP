const LambdaDeployer = require('./LambdaDeployer');

async function main() {
  const deployer = new LambdaDeployer();

  try {
    await deployer.deployLambda();
  } catch (error) {
    console.error('Lambda Deployment failed:', error);
  }
}

main();
