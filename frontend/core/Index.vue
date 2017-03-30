<template>
  <div>
    <image-section
        :title="'Do you want to improve your English?'"
        :description="'Do you have programming skills but would like to improve your English? What about connect with people who can help you to improve your English skill?&nbsp;'"
        :image="'http://wstaw.org/m/2016/02/21/english-dictionary-1559631.jpg'"
        :imageSide="'left'"></image-section>

    <image-section
        :title="'Do you want to learn how to code?'"
        :description="'Are you a native/fluent English speaker and would like to learn how to code? Here you can find who can help you while you &nbsp;teach English!'"
        :image="'http://wstaw.org/m/2016/02/21/plasma-desktopjM2067.png'"
        :imageSide="'right'"></image-section>
    
    <app-footer></app-footer>
  </div>
</template>

<script>
  import ImageSection from './components/ImageSection.vue'
  import Footer from './components/Footer.vue'
  
  export default {
    name: 'app',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    components: {
      ImageSection,
      'AppFooter': Footer
    }
  }
</script>

<style>
</style>
