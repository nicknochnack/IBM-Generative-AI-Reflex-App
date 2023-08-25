import reflex as rx

class ReflexappConfig(rx.Config):
    """Additional configuration parameters"""
    watsonx_api_key: str = 'YOUR API KEY HERE'
    watsonx_model: str = 'meta-llama/llama-2-70b-chat'
    watsonx_api_endpoint: str =  'https://bam-api.res.ibm.com/v1' # "https://workbench-api.res.ibm.com/v1"

config = ReflexappConfig(
    app_name="app",
)