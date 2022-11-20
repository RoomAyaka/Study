<?php

namespace App\Providers;

use Illuminate\Support\Facades\View;
use Illuminate\Support\ServiceProvider;

class HelloServiceProvider extends ServiceProvider
{
    public function boot()
    {
        View::composer(
            'index', function($view){
                $view->with('view_message', 'composer message!');
            }
        );
    }
}
// {
//     /**
//      * Register services.
//      *
//      * @return void
//      */
//     public function register()
//     {
//         //
//     }

//     /**
//      * Bootstrap services.
//      *
//      * @return void
//      */
//     public function boot()
//     {
//         //
//     }
// }
