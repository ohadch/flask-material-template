<template>
  <v-layout text-center align-center justify-center mt-3>
    <v-flex xs12 sm6 md6>
      <HelloWorld />
    </v-flex>
  </v-layout>
</template>

<script>
import HelloWorld from "@/components/HelloWorld";

export default {
  name: "HomePage",
  components: {
    HelloWorld
  },
};
</script>
