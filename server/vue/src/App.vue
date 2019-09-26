<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">My Website Template</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text v-if="user">
        <span class="mr-2">Hello, {{ user.username }}</span>
      </v-btn>
      <v-btn outlined v-if="user" @click="$router.push('/login')">
        <span class="mr-2">Logout</span>
      </v-btn>
    </v-app-bar>

    <v-content>
      <v-alert v-if="alert.message" :type="alert.type">{{alert.message}}</v-alert>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  computed: {
    alert() {
      return this.$store.state.alert;
    },
    user() {
      return this.$store.state.authentication.user;
    }
  },
  watch: {
    $route() {
      // clear alert on location change
      this.$store.dispatch("alert/clear");
    }
  }
};
</script>
