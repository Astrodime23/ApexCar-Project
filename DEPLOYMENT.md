# Deployment Guide: ApexCar

This guide will walk you through the process of pushing your project to GitHub and deploying the frontend on Vercel for free.

## Prerequisites
1. A GitHub account (https://github.com)
2. Git installed on your computer (https://git-scm.com/)
3. A Vercel account (https://vercel.com)

## Phase 1: Pushing Code to GitHub

1. **Initialize a Git Repository**
   Open your terminal, navigate to your project folder (`ApexCar`), and run:
   ```bash
   git init
   ```

2. **Add Your Files**
   Stage all your project files for the first commit:
   ```bash
   git add .
   ```

3. **Commit Your Changes**
   Save the state of your files with a message:
   ```bash
   git commit -m "Initial commit: ApexCar website"
   ```

4. **Create a Repository on GitHub**
   - Go to GitHub and log in.
   - Click the **+** icon in the top right corner and select **New repository**.
   - Name your repository (e.g., `apex-car`).
   - Keep it Public or Private, and leave "Initialize this repository with a README" unchecked.
   - Click **Create repository**.

5. **Link and Push**
   Copy the commands provided by GitHub under "...or push an existing repository from the command line". It will look something like this:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/apex-car.git
   git push -u origin main
   ```
   Run these commands in your terminal. Your code is now safely on GitHub!

## Phase 2: Deploying the Frontend to Vercel

Since our frontend is a static HTML file, Vercel is the perfect free hosting solution.

1. **Log in to Vercel**
   Go to [Vercel](https://vercel.com/) and log in using your GitHub account.

2. **Import Your Project**
   - Click on the **Add New...** button and select **Project**.
   - You will see a list of your GitHub repositories. Find your `apex-car` repository and click **Import**.

3. **Configure the Project**
   - Vercel will automatically detect that this is a static site.
   - You don't need to change any build settings for this setup.
   - Note: Vercel will serve the `index.html` file as a static webpage. However, Vercel's static hosting *does not* run Python backend servers like `server.py` continuously.

4. **Deploy**
   - Click the **Deploy** button.
   - Wait for a few seconds while Vercel builds and deploys your static files.

5. **Visit Your Live Site**
   - Once the deployment is complete, Vercel will provide you with a live URL (e.g., `https://apex-car.vercel.app`).
   - Click the link to see your website live on the internet!

## Important Note regarding the Backend
Currently, your frontend (`index.html`) is hardcoded to call `http://localhost:5000/api/test-drive`. For the deployed site to talk to a live backend, you would need to:
1. Host your `server.py` on a service like Render or PythonAnywhere.
2. Update the `fetch()` URL in your `index.html` from `http://localhost:5000/api/test-drive` to your new live backend URL before pushing the final version to GitHub.

---
You're all set! If you make further changes to your code locally in the future, just run `git add .`, `git commit -m "update"`, and `git push`, and Vercel will automatically rebuild and update your live site!
