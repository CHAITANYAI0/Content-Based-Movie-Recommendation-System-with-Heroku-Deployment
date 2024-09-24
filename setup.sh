mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = flase\n\
headless = true\n\
\n\
" > ~/streamlin/config.toml