const config = {
    MAX_ATTACHMENT_SIZE: 5000000,
    STRIPE_KEY: "",
    s3: {
      REGION: "",
      BUCKET: "",
    },
    apiGateway: {
      REGION: "",
      URL: "",
    },
    cognito: {
      REGION: "",
      USER_POOL_ID: "",
      APP_CLIENT_ID: "",
      IDENTITY_POOL_ID: "",
    },
  };
  
  export default config;