<script setup lang="ts">
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import Abstract from '@/components/pages/Abstract.vue';
import References from '@/components/pages/References.vue';
import GambarComponent from '@/components/pages/GambarComponent.vue';
import Tabels from '@/components/pages/Tabels.vue';

</script>

<template>
    <Tabs default-value="abstrak" class="w-full">
        <TabsList>
            <TabsTrigger value="abstrak">
                Abstrak
            </TabsTrigger>
            <TabsTrigger value="referensi">
                Referensi
            </TabsTrigger>
            <TabsTrigger value="gambar">
                Gambar
            </TabsTrigger>
            <TabsTrigger value="tabel">
                Tabel
            </TabsTrigger>
            <TabsTrigger value="pdf">
                PDF Skripsi
            </TabsTrigger>
        </TabsList>
        <TabsContent value="abstrak" class="mt-4">
            <Abstract />
        </TabsContent>
        <TabsContent value="referensi" class="mt-4">
            <References />
        </TabsContent>
        <TabsContent value="gambar" class="mt-4">
           <GambarComponent/>
        </TabsContent>
        <TabsContent value="tabel" class="mt-4">
            <Tabels/>
        </TabsContent>
        <TabsContent value="pdf" class="mt-4">
            Change your password here.
        </TabsContent>
    </Tabs>
</template>