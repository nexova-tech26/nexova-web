# Etapa 1: Construcción (Node.js)
FROM node:20-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Etapa 2: Producción (Nginx)
FROM nginx:alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
# Expone el puerto 80
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]