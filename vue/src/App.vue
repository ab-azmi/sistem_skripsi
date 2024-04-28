<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle
} from '@/components/ui/navigation-menu'
</script>

<template>
  <div class="w-full bg-blue-500 fixed top-0 h-28"></div>
  <div class="bg-gray-300/20 backdrop-blur-lg rounded-xl w-[95%] m-auto mt-7 p-7">
    <header>
      <div class="w-full flex items-center justify-between">
        <NavigationMenu>
          <NavigationMenuList class="flex gap-7 text-white">
            <NavigationMenuItem>
              <NavigationMenuTrigger class="cursor-pointer">Item One</NavigationMenuTrigger>
              <NavigationMenuContent>
                <NavigationMenuLink>Link</NavigationMenuLink>
              </NavigationMenuContent>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <NavigationMenuLink class="cursor-pointer">
                <RouterLink class="hover:bg-white/50 hover:text-blue-500 hover:rotate-90 transition-all rounded-md px-4 py-2 font-semibold" active-class="bg-white text-blue-500" to="/">Home</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <NavigationMenuLink class="cursor-pointer">
                <RouterLink class="hover:bg-white/50 hover:text-blue-500 hover:rotate-90 transition-all rounded-md px-4 py-2 font-semibold " active-class="bg-white text-blue-500" to="/research">Research</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <NavigationMenuLink class="cursor-pointer">
                <RouterLink class="hover:bg-white/50 hover:text-blue-500 hover:rotate-90 transition-all rounded-md px-4 py-2 font-semibold " active-class="bg-white text-blue-500" to="/about">About me</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <NavigationMenuLink class="cursor-pointer">
                <RouterLink class="hover:bg-white/50 hover:text-blue-500 hover:rotate-90 transition-all rounded-md px-4 py-2 font-semibold " active-class="bg-white text-blue-500" to="/demo">Demo</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>
        <div>
          <button class="bg-slate-500 text-white px-3 py-1 rounded">Logo</button>
        </div>
  
  
      </div>
    </header>
    <main class="mt-10">
      <RouterView />
    </main>
  </div>
</template>
