import { NavComponent } from '../../components/users/partials/nav/nav.component';
import { SideComponent } from '../../components/users/partials/side/side.component';


/* CONTENT ONLY LAYOUT
 * @desc : web layout view that only loads the
 *         content fully. (no navs, footer, sidebar, etc..)
 */
export function ContentOnly(content) {
  return { content };
}

/* USER NAVIGATION, CONTENT
 * @desc : web layout view that preloads the navigation bar
 *         together with the content.
 */
export function NavContent(content) {
  return {
    navigation: NavComponent,
    content
  };
}

/* USER NAVIGATION, SIDEBAR, CONTENT
 */
export function NavSideContent(content) {
  return {
    navigation: NavComponent,
    side: SideComponent,
    content
  };
}
