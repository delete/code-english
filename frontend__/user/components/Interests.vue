<template>
  <div>
    <p>
      <h4 v-if="iam == 'student'">I Want to Learn:</h4>
      <h4 v-else>I Can Teach:</h4>
    </p>
    <template v-for="interest in interests">
      <interest 
          :interest="interest"
          :iam="iam == 'student'? 'S': 'T'"></interest>
    </template>
  </div>
</template>

<script>
  import Interest from './Interest.vue'
  export default {
    props: ['interests', 'iam'],
    components: {
      Interest
    }
  }
</script>