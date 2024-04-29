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
import { useToast } from '@/components/ui/toast/use-toast'
import { useAnalyzeStore } from '@/stores/analyze'
import { Skeleton } from '@/components/ui/skeleton'
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table'

onMounted(() => {
    getRequest()
    analyzeStore.getHistoryFromLocalStorage()
})

const { toast } = useToast()
const analyzeStore = useAnalyzeStore()

const frameworks: {
    value: number,
    label: string,
}[] = []

const open = ref(false)
const value = ref<number>()
const hypoStore = useHypoStore()
const loading = ref(false)

const keterangan = ref([
    {
        value: 'entail',
        description: 'Pasangan teks surat kontrak dan hipotesis yang anda masukkan berstatus entail atau terikat. Artinya surat kontrak tersebut mendukung hipotesis yang anda masukkan.'
    },
    {
        value: 'contradict',
        description: 'Pasangan teks surat kontrak dan hipotesis yang anda masukkan berstatus contradict atau bertentangan. Artinya surat kontrak tersebut tidak mendukung hipotesis yang anda masukkan.'
    },
    {
        value: 'neutral',
        description: 'Pasangan teks surat kontrak dan hipotesis yang anda masukkan berstatus neutral atau netral. Artinya surat kontrak tersebut tidak memiliki cukup informasi untuk mendukung atau menentang hipotesis yang anda masukkan.'
    }

])

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
    form.value.hypothesis = hypoStore.hypos.find((hypo) => hypo.id === newValue)?.content ?? '';
})

// FORM

const form = ref<{
    hypothesis: string,
    contract: string,
}>({
    hypothesis: '',
    contract: '',
})

function validate() {
    if (form.value.hypothesis === '') {
        toast({
            title: 'Uh oh! Something went wrong.',
            description: 'Hypothesis cannot be empty.',
            variant: 'destructive'
        });
        return false
    }
    if (form.value.contract === '') {
        toast({
            title: 'Uh oh! Something went wrong.',
            description: 'Contract cannot be empty.',
            variant: 'destructive'
        });
        return false
    }
}
async function submitForm() {
    if (validate() === false) {
        return
    }
    loading.value = true
    toast({
        title: 'Processing...',
        description: 'Your request is being processed.',
    });

    await analyzeStore.analyzePair(form.value.contract, form.value.hypothesis)

    if (analyzeStore.error) {
        toast({
            title: 'Uh oh! Something went wrong.',
            description: 'There was a problem with your request.',
            variant: 'destructive'
        });
        return
    }

    toast({
        title: 'Success!',
        description: 'Your request has been processed.',
    });
    loading.value = false
    analyzeStore.addToHistory()
}
</script>

<template>
    <div class="flex gap-5">
        <div class="w-full">
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
                                        : "hypothesis..." }}
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

                    <form class="w-full space-y-6" @submit.prevent="submitForm">
                        <div class="flex flex-col gap-1">
                            <Textarea required v-model="form.hypothesis"
                                placeholder="Selected hypothesi will be shown here" disabled />
                        </div>
                        <div class="flex flex-col gap-2">
                            <Label for="terms">Contract</Label>
                            <Textarea required v-model="form.contract" placeholder="Type your contract here."
                                rows="15" />
                        </div>
                        <Button type="submit">
                            Submit
                        </Button>
                    </form>
                </CardContent>
            </Card>
        </div>
        <div class="w-full flex flex-col gap-5">
            <Card>
                <CardHeader>
                    <CardTitle>Hasil</CardTitle>
                </CardHeader>
                <CardContent>
                    <div v-if="loading" class="flex flex-col space-y-3">
                        <Skeleton class="h-[125px] w-full rounded-xl" />
                        <div class="space-y-2">
                            <Skeleton class="h-4 w-full" />
                            <Skeleton class="h-4 w-[40%]" />
                        </div>
                    </div>
                    <div v-else>
                        <h1 class="uppercase text-xl font-bold" :class="{
                            'text-green-500': analyzeStore.result === 'entail',
                            'text-red-500': analyzeStore.result === 'contradict',
                            'text-blue-500': analyzeStore.result === 'neutral'
                        }">
                            {{ analyzeStore.result }}
                        </h1>
                        <p class="mt-3 text-gray-500">
                            {{ keterangan.find((ket) => ket.value === analyzeStore.result)?.description }}
                        </p>
                    </div>
                </CardContent>
            </Card>
            <Card>
                <CardHeader>
                    <CardTitle>Riwayat</CardTitle>
                </CardHeader>
                <CardContent>
                    <Table>
                        <TableCaption>Riwayat analisis yang anda lakukan</TableCaption>
                        <TableHeader>
                            <TableRow>
                                <TableHead>
                                    Waktu
                                </TableHead>
                                <TableHead>Hasil</TableHead>
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            <TableRow v-for="ref in analyzeStore.history" :key="ref.timestamp">
                                <TableCell class="font-medium">
                                    {{ new Date(ref.timestamp).toLocaleString() }}
                                </TableCell>
                                <TableCell>
                                    <p class="uppercase" :class="{
                                        'text-green-500': ref.result === 'entail',
                                        'text-red-500': ref.result === 'contradict',
                                        'text-blue-500': ref.result === 'neutral'
                                    }">
                                        {{ ref.result }}
                                    </p>
                                </TableCell>

                            </TableRow>
                        </TableBody>
                    </Table>
                </CardContent>
            </Card>

        </div>
    </div>
</template>