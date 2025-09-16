FROM node:24-alpine AS builder
WORKDIR /app
COPY ./package.json ./package-lock.json ./
RUN npm install
COPY . .
RUN npx vite build

FROM nginx:stable-alpine AS runner
WORKDIR /app
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
CMD [ "nginx", "-g", "daemon off;" ]