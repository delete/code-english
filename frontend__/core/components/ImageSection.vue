<template>
  <div class="section">
    <div class="container">
      <div class="row">
        <div class="col-md-6" v-if="imageSide == 'left'">
          <img :src="image" class="img-responsive">
        </div>
        <div class="col-md-6">
          <h1 class="text-primary">{{ title }}</h1>
          <h3></h3>
          <p class="description">{{ description }}</p>
        </div>
        <div class="col-md-6" v-if="imageSide == 'right'">
          <img :src="image" class="img-responsive">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      'title': String,
      'description': String,
      'image': String,
      'imageSide': String
    }
  }
</script>