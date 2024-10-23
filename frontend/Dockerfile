# Use an official Node.js image as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files into the container
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

# Install any dependencies specified in package.json
RUN npm install

# Copy the rest of the application code into the container
COPY . /app

# Build the React app for production
RUN npm run build

# Use an official Nginx image to serve the built app
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html

# Expose port 80 for the web server
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
