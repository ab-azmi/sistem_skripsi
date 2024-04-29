<script setup lang="ts">
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table'


const references = [
    {
        peneliti: 'Ivgi dkk., (2022)',
        judul: 'Efficient Long-Text Understanding with Short-Text Models',
        url: 'https://arxiv.org/abs/2208.00748',
    },
    {
        peneliti: 'Koreeda & Manning, (2021)',
        judul: 'ContractNLI: A Dataset for Documentlevel Natural Language Inference for Contracts.',
        url: 'https://aclanthology.org/2021.findings-emnlp.164/'
    },
    {
        peneliti: 'Shaham dkk., (2022)',
        judul: 'SCROLLS: Standardized CompaRison Over Long Language Sequences',
        url: 'https://arxiv.org/abs/2201.03533v2'
    },
    {
        peneliti: 'Ainslie dkk., (2023)',
        judul: 'CoLT5: Faster Long-Range Transformers with Conditional Computation',
        url: 'https://arxiv.org/abs/2303.09752v3'
    },
    {
        peneliti: 'Bertsch dkk., (2023)',
        judul: 'Unlimiformer: Long-Range Transformers with Unlimited Length Input',
        urL: 'https://arxiv.org/abs/2305.01625v3'
    },
    {
        peneliti: 'Tay dkk., (2023) ',
        judul: 'UL2: Unifying Language Learning Paradigms',
        url: 'https://arxiv.org/abs/2205.05131v3',
    },
    {
        peneliti: 'Servan dkk., (2024)',
        judul: 'mALBERT: Is a Compact Multilingual BERT Model Still Worth It?',
        url: 'https://arxiv.org/abs/2403.18338v1'
    },
    {
        peneliti: 'Fu dkk., (2023)',
        judul: 'Energy-efficient Task Adaptation for NLP Edge Inference Leveraging Heterogeneous Memory Architectures',
        url: 'https://arxiv.org/abs/2303.16100'
    },
    {
        peneliti: 'Naseem dkk., (2020)',
        judul: 'BioALBERT: A Simple and Effective Pre-trained Language Model for Biomedical Named Entity Recognition',
        url: 'https://ieeexplore.ieee.org/document/9533884'
    },
    {
        peneliti: 'Cã Nete dkk., (2022)',
        judul: 'ALBETO and DistilBETO: Lightweight Spanish Language Models',
        url: 'https://aclanthology.org/2022.lrec-1.457/'
    }
]
</script>

<template>
    <Table>
        <TableCaption>List referensi utama yang dipakai dalam penelitian.</TableCaption>
        <TableHeader>
            <TableRow>
                <TableHead>
                    Peneliti
                </TableHead>
                <TableHead>Judul</TableHead>
                <TableHead class="text-right">
                    Url
                </TableHead>
            </TableRow>
        </TableHeader>
        <TableBody>
            <TableRow v-for="ref in references">
                <TableCell class="font-medium">
                    {{ ref.peneliti }}
                </TableCell>
                <TableCell>
                    {{ ref.judul }}
                </TableCell>
                <TableCell class="text-right">
                    <a :href="ref.url" target="_blank" rel="noopener noreferrer"
                        class="bg-primary px-3 py-2 rounded-md text-white">
                        visit
                    </a>
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>