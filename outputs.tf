output "lamda_arn" {
  description = "Lamda ARN"
  value       = module.lambda_function.lambda_function_invoke_arn
}

output "base_url" {
  description = "Base URL for API Gateway stage."

  value = aws_apigatewayv2_stage.lambda.invoke_url
}


output "function_name" {
  description = "Name of the Lambda function."

  value = module.lambda_function.lambda_function_name
}
