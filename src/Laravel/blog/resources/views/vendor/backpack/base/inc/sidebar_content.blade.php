{{-- This file is used to store sidebar items, inside the Backpack admin panel --}}
<li class="nav-item"><a class="nav-link" href="{{ backpack_url('dashboard') }}"><i class="la la-home nav-icon"></i> {{ trans('backpack::base.dashboard') }}</a></li>

<li class="nav-item"><a class="nav-link" href="{{ backpack_url('tag') }}"><i class="nav-icon la la-question"></i> Tags</a></li>
<li class="nav-item"><a class="nav-link" href="{{ backpack_url('news') }}"><i class="nav-icon la la-question"></i> News</a></li>
<li class="nav-item"><a class="nav-link" href="{{ backpack_url('blog') }}"><i class="nav-icon la la-question"></i> Blogs</a></li>