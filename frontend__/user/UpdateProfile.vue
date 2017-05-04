<template>
  <div class="section">
    <p>{{message}}</p>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h1>Update your profile</h1>

          <form>
            <div class="form-group">
              <label>Full name</label>
              <input type="text" v-model="full_name">
            </div>
            <div class="form-group">
              <label>Country</label>
              <input type="text" v-model="country">
            </div>

            <input id="token" type="hidden" :value="token">

            <div class="form-inline">
              <button class="btn btn-primary form-control" @click.prevent="submit">
                <i class="fa fa-floppy-o"></i> 
                Submit</button>                
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { HTTP } from '../main'
  export default {
    data() {
      return {
        full_name: '',
        country: '',
        token: '',
        message: ''
      }
    },
    mounted(){
      this.token = this.getCookie('csrftoken')
    },
    props: {
      user: [String, Number]
    },
    methods: {
      getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for(var i = 0; i <ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
      },
      submit() {
        var self = this;
        HTTP.defaults.headers.common['X-CSRFToken'] = this.token
        HTTP.post('/login/update_profile/', {
          full_name: this.full_name,
          country: this.country
        })
        .then(function (response) {
          self.message = response.data.message
          console.log(response.data)
          setTimeout(function() {
            window.location = '/login/dashboard/'
          }, 2000);
        })
        .catch(function (error) {
          console.log(error)
        })
      }
    }
  }
</script>
