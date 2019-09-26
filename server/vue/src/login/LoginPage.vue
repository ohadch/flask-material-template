<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-form @submit.prevent="handleSubmit">
            <v-toolbar color="primary" dark flat>
              <v-toolbar-title>Login form</v-toolbar-title>
              <div class="flex-grow-1"></div>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                label="Username"
                name="username"
                prepend-icon="person"
                type="text"
                v-model="username"
              ></v-text-field>
              <v-text-field
                v-model="password"
                id="password"
                label="Password"
                name="password"
                prepend-icon="lock"
                type="password"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <div class="flex-grow-1"></div>
              <v-btn :loading="loggingIn" type="submit" color="primary">Login</v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      username: "",
      password: "",
      submitted: false
    };
  },
  created() {
    // reset login status
    this.$store.dispatch("authentication/logout");
  },
  computed: {
    loggingIn() {
      return this.$store.state.authentication.status.loggingIn;
    }
  },
  methods: {
    handleSubmit() {
      this.submitted = true;
      const { username, password } = this;
      const { dispatch } = this.$store;
      if (username && password) {
        dispatch("authentication/login", { username, password });
      }
    }
  }
};
</script>
