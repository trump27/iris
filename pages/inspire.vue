<template>
  <v-flex xs10 sm10 md10>
    <h2 class="ma-2">IRIS 学習データ</h2>
    <v-data-table :headers="headers" :items="iris" :rows-per-page-items="pagni" class="elevation-1">
      <template v-slot:items="props">
        <td class="text-xs-right">{{ props.item.sepal_length }}</td>
        <td class="text-xs-right">{{ props.item.sepal_width }}</td>
        <td class="text-xs-right">{{ props.item.petal_length }}</td>
        <td class="text-xs-right">{{ props.item.petal_width }}</td>
        <td class="text-xs-right">{{ props.item.target }}</td>
      </template>
    </v-data-table>
  </v-flex>
</template>

<script>
import iris from '@/components/iris.json'
export default {
  data() {
    return {
      iris: [],
      headers: [
        { text: 'sepal_length', value: 'sepal_length' },
        { text: 'sepal_width', value: 'sepal_width' },
        { text: 'petal_length', value: 'petal_length' },
        { text: 'petal_width', value: 'petal_width' },
        { text: 'target', value: 'target' }
      ],
      pagni: [
        20,
        50,
        75,
        { text: '$vuetify.dataIterator.rowsPerPageAll', value: -1 }
      ]
    }
  },
  mounted() {
    this.iris = iris
    // console.log(iris)
  }
}
</script>
