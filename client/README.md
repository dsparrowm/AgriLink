# Agrilink client

The Client folder contains everything Front end. Here you will find the client faceing site code base, setups and configurations. The Front End langauge used is [NuxtJS](https://v2.nuxt.com/) - The Intuitive Vue Framework.

## Features

- Modern and cross-broswer compatibility designs: With the help of [BootstrapVue](https://bootstrap-vue.org/).
- Responsiveness: This project follows the mobile first Website Development approach.
- Asynchronous data-fetching: [nuxt/axios](https://axios.nuxtjs.org/) - Uses [Axios](https://github.com/axios/axios) (Promise based HTTP client for the browser and node.js) for making asynchronous APIs calls.
- User registeration and authentication: [nuxt/auth](https://auth.nuxtjs.org/) - The module authenticates users using a configurable authentication [scheme](https://auth.nuxtjs.org/guide/scheme).
- Product listing: List all products in database per page or list products by category.
- User profile: Users can easily view, manage or update their profile informations.
- Order placement and Payment: Buyers can place orders and easily make payment - with the help of [Flutterwave Vue.JS (Vue2) Library](https://github.com/Flutterwave/Vue-v3).
- Farmer Dashboard: Farmer only page. After logging in, the user (that is, farmer) is redirected to his/her dashboard. where they are able to view sales analysis, view performance summary of each product on display in chart form, view orders (pending and completed), add new products on display, update product details, and more.

## Important Routes/Pages

- `/`: Agrilink welcome/landing page.
- `/products/`: Product listing page.
   - `?category=all`: list all product.
   - `?category=<:name>`: list products by category name.
- `/product/details`: Displays a more detail information about the selected product.
- `/profile`: displays current logged in user information. 
- `/dashboard`: only accessible to farmers.
- `/orders/`: list current users orders (that is, pending or completed).

## Dependencies

Some Important Front-end technologies:

| Tools/Library          | Version |
| ---------------------- |:-------:|
|  [vue]                 | ^2.7.10 |
|  [nuxt]                | ^2.15.8 |
|  [nuxtjs/auth]         | ^4.9.1  |
|  [flutterwave-vue-v3]  | ^1.0.9  |
|  [nuxtjs/google-fonts] | ^3.0.1  |
|  [vue-fontawesome]     | ^2.0.6  |
|  [bootstrap-vue]       | ^2.22.0 |
|  [vue-chartjs]         | ^4.1.1  |

view the complete list of front-end dependencies in the corresponding [package.json].

Packaging/Deployment:
| Tools/Library  | Version  |
| -------------- |:--------:|
|  [node]        | ^14.20.0 |
|  [npm]         | ^6.14.17 |


[vue]: https://vuejs.org/
[nuxt]: https://v2.nuxt.com/
[nuxtjs/auth]: https://auth.nuxtjs.org/
[flutterwave-vue-v3]: https://github.com/Flutterwave/Vue-v3
[nuxtjs/google-fonts]: https://google-fonts.nuxtjs.org/
[vue-fontawesome]: https://fontawesome.com/docs/web/use-with/vue/
[bootstrap-vue]: https://bootstrap-vue.org/
[vue-chartjs]: https://vue-chartjs.org/guide/
[package.json]: https://github.com/dsparrowm/AgriLink/blob/Development/client/package.json
[node]: https://nodejs.org/docs/latest-v14.x/api/
[npm]: https://nodejs.org/docs/latest-v14.x/api/

## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

## Author
- Daniel Enagu [linkedIn handle](https://www.linkedin.com/in/enagudaniel/)