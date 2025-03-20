# Use the official Node.js image
FROM node:16
# Inject from the Doppler
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Build the React app
RUN npm run build

# Install `serve` to serve the React app
RUN npm install -g serve

# Expose port 5000 (default port for React apps)
EXPOSE 3030

# Serve the React app
CMD ["serve", "-s", "build", "-l", "3030"]