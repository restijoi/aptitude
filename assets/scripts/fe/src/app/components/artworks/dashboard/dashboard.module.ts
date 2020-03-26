import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { UIRouterModule } from '@uirouter/angular';
import { NgxDropzoneModule } from 'ngx-dropzone';

import { HomeComponent } from './home/home.component';
import { CreateComponent } from './create/create.component';

@NgModule({
  declarations: [HomeComponent, CreateComponent],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    UIRouterModule,
    NgxDropzoneModule,
  ]
})
export class DashboardModule { }
