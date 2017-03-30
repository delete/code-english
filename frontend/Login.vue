<template>
  <div>
    <h1>{{msg}}</h1>
    <p v-for="name in names">{{name}}</p>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        msg: 'Welcome to login'
      }
    },
    props: ['names']
  }
</script>

<style scoped>
  div {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  h1{
    font-weight: normal;
  }
</style>
