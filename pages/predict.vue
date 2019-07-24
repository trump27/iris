<template>
  <div>
    <h2 class="mt-2">あやめ（IRIS）品種の予測</h2>
    <h3 class="mt-2">特徴量</h3>
    <v-card-actions>
      <v-spacer />
      <v-btn color="primary" nuxt to="/irisdata">IRISの学習データ</v-btn>
    </v-card-actions>
    <v-form>
      <v-container>
        <v-layout row wrap>
          <v-flex xs10 sm5 md3>
            <v-text-field
              v-model="sepal_length"
              label="萼(がく)の長さ ㎝"
              type="Number"
              :rules="[rules.required]"
              clearable
            ></v-text-field>
          </v-flex>
          <v-flex xs10 sm5 md3>
            <v-text-field
              v-model="sepal_width"
              label="萼(がく)の幅 ㎝"
              type="Number"
              :rules="[rules.required]"
              clearable
            ></v-text-field>
          </v-flex>
        </v-layout>

        <v-layout row wrap>
          <v-flex xs10 sm5 md3>
            <v-text-field
              v-model="petal_length"
              label="花弁の長さ ㎝"
              type="Number"
              :rules="[rules.required]"
              clearable
            ></v-text-field>
          </v-flex>
          <v-flex xs10 sm5 md3>
            <v-text-field
              v-model="petal_width"
              label="花弁の幅 ㎝"
              type="Number"
              :rules="[rules.required]"
              clearable
            ></v-text-field>
          </v-flex>
        </v-layout>
      </v-container>
    </v-form>
    <v-btn
      @click="predict"
      :disabled="!sepal_length || !sepal_width || !petal_length || !petal_width"
      color="info"
    >予測API</v-btn>

    {{api}}
    <v-card class="mt-4">
      <v-toolbar card color="pink" dark>
        <v-toolbar-title>予測API結果</v-toolbar-title>
      </v-toolbar>
      <v-text-field value="IRIS品種予測" single-line full-width hide-details></v-text-field>
      <v-text-field single-line full-width v-model="prediction" hide-details box></v-text-field>
      <v-divider />
      <v-text-field value="予測確率" single-line full-width hide-details></v-text-field>
      <v-text-field single-line full-width v-model="proba" hide-details box></v-text-field>
    </v-card>

    <v-snackbar v-model="snackbar" :color="color" :top="true" :timeout="2000" :vertical="false">
      {{ msg }}
      <v-btn dark flat @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
import config from './config.js'
export default {
  data() {
    return {
      sepal_length: 5.32,
      sepal_width: 3,
      petal_length: 4,
      petal_width: 3.3,
      rules: {
        required: v => !!v || 'This field is required'
      },
      snackbar: false,
      msg: 'api called.',
      color: 'primary',
      // mode: 'vertical',
      prediction: null,
      proba: null,
      class: { 0: 'setosa', 1: 'versicolor', 2: 'virginica' },
      api: null
    }
  },
  mounted() {
    this.api = config.api_host
  },
  methods: {
    async predict() {
      let self = this
      console.log('host: ', config.api_host)

      let result = null
      try {
        result = await this.$axios.$post(config.api_host + '/predict', {
          feature: [
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width
          ]
        })
        console.log('response: ', result)
      } catch (error) {
        window.alert('cannot connect api server')
        console.log('error: ', error)
        return
      }
      this.snackbar = true
      this.prediction = this.class[result.predict]
      this.proba = result.proba
    }
  }
}
</script>

<style>
</style>
