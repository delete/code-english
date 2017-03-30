<template>
  <div class="cover">
    
    <navbar></navbar>
    
    <div class="cover-image" style="background-image : url('https://ununsplash.imgix.net/uploads/14127101912749510b8ed/82743738?w=1024&amp;q=50&amp;fm=jpg&amp;s=2150993787c74416103059d6ebac09f5')"></div>
    <div class="container">
      <div class="row">
        <div class="col-md-12 text-center">
          <h1 class="text-primary">Code &amp; English</h1>
          <p class="text-primary size">Share your English and programming skills</p>
          <br>
          <br>
          <a href="{% url 'users:signup' %}" class="btn btn-lg btn-primary size">
            sign up<br>
          </a>
          <a href="{% url 'users:login' %}" class="btn btn-lg btn-primary size">
            login<br>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Navbar from './Navbar.vue'

  export default {
    components: {
      Navbar
    }
  }
</script>