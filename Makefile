.PHONY: build

build:
	sam build

deploy-site:
	cd portfoliowebsite/ && bundle exec jekyll clean
	cd portfoliowebsite/ && bundle exec jekyll build
	aws-vault exec $$PORTFOLIO_USER --no-session -- aws s3 sync portfoliowebsite/_site s3://$$PORTFOLIO_S3_BUCKET



deploy-infra:
	make build; \
	aws-vault exec $$PORTFOLIO_USER --no-session -- \
	sam deploy \
	--parameter-overrides \
		ParameterKey=PortfolioBucketName,ParameterValue=$$PORTFOLIO_S3_BUCKET \
		ParameterKey=PortfolioDomainNameParameter,ParameterValue=$$PORTFOLIO_DOMAIN_NAME \
		ParameterKey=PortfolioHostedZoneParameter,ParameterValue=$$PORTFOLIO_HOSTED_ZONE_ID \
		ParameterKey=PortfolioCertificateArn,ParameterValue=$$PORTFOLIO_CERTIFICATE_ARN \
		ParameterKey=CounterTableName,ParameterValue=$$PORTFOLIO_COUNTER_TABLE_NAME \
		ParameterKey=IpTableName,ParameterValue=$$PORTFOLIO_IP_TABLE_NAME \
		ParameterKey=ApiCertificateArnParameter,ParameterValue=$$PORTFOLIO_API_CERTIFICATE_ARN \


invoke-update-counter:
	sam build && aws-vault exec $$PORTFOLIO_USER --no-session -- sam local invoke UpdateCounterFunction

# deploy-infra-init-only:
# 	make build; \
# 	aws-vault exec $$PORTFOLIO_USER --no-session -- \
# 		sam deploy --guided \
# 			--parameter-overrides \
# 				ParameterKey=PortfolioBucketName,ParameterValue=$$PORTFOLIO_S3_BUCKET
