const VueLoaderPlugin = require('vue-loader/lib/plugin')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    mode: 'development',
    entry: '.apps/frontend/js/index.js',
    output: {
        filename: '[name].[hash].bundle.js',
        path: path.resolve(__dirname, '/apps/frontend/dist'),
        publicPath: '/static/dist/'
    },
    plugins: [
        new VueLoaderPlugin(),
        new BundleTracker('./apps/webpack-stats.json'),
    ],

    module: {
        rules: [
            { test: /\.css$/, use: ['style-loader', 'css-loader']},
            { test: /\.vue$/, use: 'vue-loader'},
            { test: /.*\.(png|jpe?g)$/, use: 'file-loader'}
        ]
    }
}