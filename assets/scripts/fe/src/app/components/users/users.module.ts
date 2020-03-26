import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UIRouterModule } from '@uirouter/angular';

import { NavComponent } from './partials/nav/nav.component';
import { SideComponent } from './partials/side/side.component';



@NgModule({
  declarations: [ 
    NavComponent, 
    SideComponent
  ],
  imports: [
    CommonModule,
    UIRouterModule
  ]
})
export class UsersModule { }
