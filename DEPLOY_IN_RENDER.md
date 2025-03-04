# Deploying Async ImageGen Bot on Render

Render is a free, container-based hosting platform with a generous free tier that is ideal for deploying long-running applications like your Telegram bot. This guide will walk you through deploying the Async ImageGen Bot using Render.

## Prerequisites

- A GitHub repository containing your bot’s complete source code.
- A Dockerfile in your repository (see [Dockerfile](./Dockerfile)) that builds your bot application.
- Environment variables set in Render for sensitive credentials:
  - `TELEGRAM_TOKEN`
  - `HF_API_TOKEN`
  - `REDIS_HOST` (if using a managed Redis service or your own hosting)

## Step-by-Step Deployment

### 1. Push Your Code to GitHub

If you haven’t done so already, initialize your Git repository, add your files, and push them to GitHub:

```bash
# Change to your project directory
cd /path/to/your/project

# Initialize Git repository and commit your files
git init
git add .
git commit -m "Initial commit for Async ImageGen Bot"

# Add your GitHub repository as remote and push
git remote add origin https://github.com/yourusername/async-imagegen-bot.git
git push -u origin master
```

### 2. Create a New Web Service on Render

1. Log in to Render and go to the **Dashboard**.
2. Click on **New** > **Web Service**.
3. Connect your GitHub account if you haven’t already and select the `async-imagegen-bot` repository.
4. In the **Configure Service** screen:
   - **Name:** Provide a name for your service.
   - **Environment:** Select **Docker**.
   - **Branch:** Choose the branch you want to deploy (e.g., `master`).
   - **Build Command:** Keep it empty if your Dockerfile takes care of building.
   - **Start Command:** Ensure your Dockerfile CMD (e.g., `python main.py`) is correctly set. Render uses your Dockerfile by default.
5. **Advanced Settings:**
   - Set the **Plan** to the Free tier.
   - Under **Environment Variables**, add:
     - `TELEGRAM_TOKEN` = _your telegram bot token_
     - `HF_API_TOKEN` = _your huggingface API token_
     - `REDIS_HOST` = _if applicable (for example, use your managed Redis app or "redis" if linking with Render Redis)_
     - Other environment variables as needed.

### 3. Deploy Your Service

After configuring, click **Create Web Service**. Render will clone your GitHub repository, build the Docker image according to your Dockerfile, and deploy the container.

You can monitor the build logs and deployment status from your Render dashboard. Once the build is complete, your Telegram bot will be running on Render.

### 4. Testing and Updates

- **Testing:** Interact with your Telegram bot using the Telegram app to verify that commands like `/start`, `/flux`, `/stable`, and `/both` work as expected.
- **Updates:** Push any code changes to your GitHub repository. Render will automatically rebuild and redeploy your service if auto-deploy is enabled.

## Additional Tips

- **Scaling:** Render allows you to scale your service easily if your bot becomes popular.
- **Monitoring:** You can integrate Render’s built-in monitoring tools or external services for logging and performance tracking.
- **Security:** Always ensure that sensitive tokens and API keys are managed via environment variables and not hard-coded.

By following these steps, your Async ImageGen Bot will be up and running on Render, providing fast and reliable performance on a scalable, free hosting platform.

Happy Deploying!