<script setup lang="ts">
import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
} from '@/components/ui/card'
import { ref, onMounted, watch } from 'vue'
import { Check, ChevronsUpDown } from 'lucide-vue-next'
import { useHypoStore } from '@/stores/hypo'

import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import {
    Command,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList,
} from '@/components/ui/command'
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from '@/components/ui/popover'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'

onMounted(() => {
    getRequest()
})

const frameworks: {
    value: number,
    label: string,
}[] = []

const open = ref(false)
const value = ref<number>()
const hypoStore = useHypoStore()
const selectedHypo = ref<string>()

async function getRequest() {
    await hypoStore.getHypos()
    hypoStore.hypos.forEach((hypo) => {
        frameworks.push({
            value: hypo.id,
            label: hypo.name
        })
    })
}
//watch value
watch(value, (newValue: number | undefined) => {
    //set form schema hypothesis value
    selectedHypo.value = hypoStore.hypos.find((hypo) => hypo.id === newValue)?.content
})
// FORM


</script>

<template>
    <div class="flex">
        <div class="w-[50%]">
            <Card>
                <CardHeader>
                    <CardTitle>CNLI Textual Entailment</CardTitle>
                </CardHeader>
                <CardContent>
                    <div class="flex flex-col gap-2 mb-3">
                        <Label for="terms">Select Hypothesis</Label>
                        <Popover v-model:open="open">
                            <PopoverTrigger as-child>
                                <Button variant="outline" role="combobox" :aria-expanded="open"
                                    class="w-full justify-between">
                                    {{ value
                                        ? frameworks.find((framework) => framework.value == value)?.label
                                        : "Select framework..." }}
                                    <ChevronsUpDown class="ml-2 h-4 w-4 shrink-0 opacity-50" />
                                </Button>
                            </PopoverTrigger>
                            <PopoverContent class="w-full p-0">
                                <Command>
                                    <CommandInput class="h-9" placeholder="Search framework..." />
                                    <CommandEmpty>No framework found.</CommandEmpty>
                                    <CommandList>
                                        <CommandGroup>
                                            <CommandItem v-for="framework in frameworks" :key="framework.value"
                                                :value="framework.value" @select="(ev) => {
                                                    if (typeof ev.detail.value === 'number') {
                                                        value = ev.detail.value
                                                    }
                                                    open = false
                                                }">
                                                {{ framework.label }}
                                                <Check :class="cn(
                                                    'ml-auto h-4 w-4',
                                                    value == framework.value ? 'opacity-100' : 'opacity-0',
                                                )" />
                                            </CommandItem>
                                        </CommandGroup>
                                    </CommandList>
                                </Command>
                            </PopoverContent>
                        </Popover>
                    </div>

                    <form class="w-full space-y-6">
                        <div class="flex flex-col gap-1">
                            <Textarea v-model="selectedHypo" placeholder="Selected hypothesi will be shown here"
                                disabled />
                        </div>
                        <div class="flex flex-col gap-2">
                            <Label for="terms">Contract</Label>
                            <Textarea placeholder="Type your contract here." rows="15"/>
                        </div>
                        <Button type="submit">
                            Submit
                        </Button>
                    </form>
                </CardContent>
            </Card>
        </div>
    </div>
</template>