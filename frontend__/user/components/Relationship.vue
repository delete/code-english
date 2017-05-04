<template>
  <div class="container">
    <template v-if="list.length">
      <div class="row">
        <div class="col-md-12">
          <h1 v-if="iam === 'teaching'" class="text-center">You are teaching to</h1>
          <h1 v-else class="text-center">You are learning from</h1>
        </div>
      </div>
      <div class="row">
        <template v-for="item in list">
            <div class="col-md-2">
              <img class="img-circle img-responsive" src="http://pingendo.github.io/pingendo-bootstrap/assets/user_placeholder.png">
            </div>

            <div v-if="iam === 'teaching'" class="col-md-4">
              <h3 class="text-left">{{ item.student }}</h3>
              <p class="text-left">Teaching: {{ item.teach }}</p>
            </div>
            <div v-else class="col-md-4">
              <h3 class="text-left">{{ item.teacher }}</h3>
              <p class="text-left">Learning: {{ item.teach }}<br></p>
            </div>
        </template>
      </div>
    </template>
    <template v-else>
      <div class="row">
        <h1 class="text-center">Nothing to show by now</h1>
      </div>
    </template>
  </div>
</template>

<script>
  export default {
    props: {
      'list': {
        required: true,
        coerce(val) {
          return JSON.parse(val) // cast the value to Object
        }
      },
      'iam': {
        required: true
      }
    }
  }
</script>