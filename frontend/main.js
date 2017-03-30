import Vue from 'vue'
import Login from './Login.vue'

import Index from './core/Index.vue'
import Cover from './core/components/Cover.vue'

// Global components (pages)
Vue.component('Index', Index)
Vue.component('Login', Login)

// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  // Base html components
  components: {
    Cover
  }
})