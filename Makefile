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
				ParameterKey=PortfolioBucketName,ParameterValue=$$PORTFOLIO_S3_BUCKET



# deploy-infra-init-only:
# 	make build; \
# 	aws-vault exec $$PORTFOLIO_USER --no-session -- \
# 		sam deploy --guided \
# 			--parameter-overrides \
# 				ParameterKey=PortfolioBucketName,ParameterValue=$$PORTFOLIO_S3_BUCKET
