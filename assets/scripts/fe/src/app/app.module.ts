import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { UIRouterModule } from '@uirouter/angular';

import { TokenService } from './commons/services/auth/interceptors/token.service';
import { APP_STATES } from './commons/utils/app.states';
import { AppComponent } from './app.component';

import { PublicModule } from './components/public/public.module';
import { DashboardModule } from './components/artworks/dashboard/dashboard.module';


@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    UIRouterModule.forRoot(APP_STATES),

    PublicModule,
    DashboardModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: TokenService, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
