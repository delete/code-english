<template>
  <div v-if="interest.iam === iam">
    <p> 
      {{ interest.subject }} - 
      <span class="badge">{{ setLevel }}</span>
    </p>
  </div>
</template>

<script>
  export default {
    props: ['interest', 'iam'],
    computed: {
      setLevel() {
        const level = this.interest.level
        if ( level == 0 ) {
          return 'Basic'
        } else if ( level == 1 ) {
          return 'Intermediate'
        } else {
          return 'Advanced'
        }
      }
    }
  }
</script>