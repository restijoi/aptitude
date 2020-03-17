import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { UIRouterModule } from '@uirouter/angular';

import { APP_STATES } from './commons/utils/app.states';
import { AppComponent } from './app.component';

import { PublicModule } from './components/public/public.module';
// import { NavComponent } from './components/users/partials/nav/nav.component';
// import { SideComponent } from './components/users/partials/side/side.component';


@NgModule({
  declarations: [
    AppComponent,
    // NavComponent,
    // SideComponent,

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    UIRouterModule.forRoot(APP_STATES),

    PublicModule,
  ],
  providers: [
    // { provide: HTTP_INTERCEPTORS, useClass: TokenService, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
