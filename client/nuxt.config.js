export default {
  ssr: false,
  // Global page headers: https://go.nuxtjs.dev/config-head
  target: 'server',
  // target: 'static',

  head: {
    title: 'AgriLink',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      // {
      //   rel: 'stylesheet',
      //   href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'
      // }
    ]
  },
  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/styles/main.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins

  plugins: [
    { src: '~/plugins/flutterwave', mode: 'client' },
    { src: '~/plugins/chart.js', mode: 'client' }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/fontawesome'
  ],
  fontawesome: {
    icons: {
      solid: true,
      brands: true
    }
  },
  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/proxy',
    '@nuxtjs/dotenv'
  ],
  axios: {
    // proxy: true
    baseURL: 'http://127.0.0.1:5000/'
  },

  auth: {
    localStorage: true,
    strategies: {
      local: {
        endpoints: {
          login: {
            url: '/login',
            method: 'post',
            propertyName: 'token'
          },
          user: {
            url: '/user',
            method: 'get',
            propertyName: false
          },
          logout: false
        }
      }
    }
    // redirect: {
    //   login: '/login',
    //   logout: false,
    //   callback: '/login',
    //   home: '/'
    // }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
};
