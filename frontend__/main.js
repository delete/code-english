import axios from 'axios'

import Vue from 'vue'

// User components
import UpdateProfile from './user/UpdateProfile.vue'
import Dashboard from './user/Dashboard.vue'

// Core components
import Index from './core/Index.vue'
import Cover from './core/components/Cover.vue'

// Registry Global components (pages)

// User
Vue.component('UpdateProfile', UpdateProfile)
Vue.component('Dashboard', Dashboard)

// Core
Vue.component('Index', Index)


export const HTTP = axios.create({
  headers: {
    common: {
      'HTTP_X_CSRFTOKEN': ''
    }
  }
})


// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  // Base html components (like header, footer, navbar, ...)
  components: {
    Cover
  }
})
