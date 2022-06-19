FROM nginx:1.21.3-alpine
ADD ./default.conf.template /etc/nginx/conf.d/default.conf.template
ADD ./uwsgi_params /etc/nginx/uwsgi_params
EXPOSE 8000
# Nginxの設定に必要なappコンテナのホスト情報の埋め込みとnginxをフォアグラウンドで起動
CMD envsubst '$$PYTHON_HOST'< /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'
