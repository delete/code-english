<template>
<div>
  <div class="jumbotron">
    <div class="row">
      <div class="col-md-12">
        <div class="section">
          <div class="container">
            <div class="row">
              <div class="col-md-3"><img class="img-responsive" src= "http://pingendo.github.io/pingendo-bootstrap/assets/user_placeholder.png">
              </div>

              <div class="col-md-9">
                <h1>{{ userFullName }}</h1>

                <div class="col-md-12">
                  <my-interests
                      :iam="'teacher'"
                      :interests="interests"></my-interests>

                  <my-interests
                      :iam="'student'" 
                      :interests="interests"></my-interests>
                </div>
                <div class="form-inline">
                  <div class="form-group">
                    <a href="" class="btn btn-primary form-control">Update Profile</a> 
                  </div>
                  <div class="form-group">
                    <a href="" class="btn btn-primary form-control">Update Interests</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="section text-center">
    <div class="container">
      <div class="row">
        <div class="div-center col-md-6 col-md-offset-3 text-center">
          <a class="btn btn-block btn-primary">Explore</a>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <relationship
        :list="teachingTo"
        :iam="'teaching'"></relationship>
  </div>

  <div class="section">
    <relationship
        :list="learningFrom"
        :iam="'learning'"></relationship>
  </div>
</div>
</template>

<script>
  import MyInterests from './components/Interests.vue'
  import Relationship from './components/Relationship.vue'
  import axios from 'axios'
  export default {
    components: {
      MyInterests,
      Relationship
    },
    props: [
      'interests',
      'userFullName',
      'teachingTo',
      'learningFrom'
    ]
  }
</script>
