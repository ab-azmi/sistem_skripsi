import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useHypoStore = defineStore("hypo", () => {
  const hypos = ref<{
    id: number;
    name: string;
    content: string;
  }[]>([]);
  const hypoCount = computed(() => hypos.value.length);

  async function getHypos() {
    // Send a request to the server to get the hypos
    const response = await fetch('http://127.0.0.1:8000/hypothesis/');

    // Check if the request was successful
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response body as JSON
    const data = await response.json();

    // Update the hypos state
    hypos.value = data;

  }

    return { hypos, hypoCount, getHypos };
});
