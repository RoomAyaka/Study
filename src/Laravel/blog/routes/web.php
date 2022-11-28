<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HelloController;
use App\Http\Middleware\HelloMiddleware;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});
// Route::get('hello/', 'App\Http\Controllers\HelloController@index')
//     -> middleware(HelloMiddleware::class);
// Route::get('hello/add/', 'App\Http\Controllers\HelloController@add');
// Route::post('hello/add/', 'App\Http\Controllers\HelloController@create');

Route::get('hello','App\Http\Controllers\HelloController@index')-> middleware(HelloMiddleware::class);
Route::post('hello','App\Http\Controllers\HelloController@post');
Route::get('hello/add','App\Http\Controllers\HelloController@add');
Route::post('hello/add','App\Http\Controllers\HelloController@create');
Route::get('hello/edit','App\Http\Controllers\HelloController@edit');
Route::post('hello/edit','App\Http\Controllers\HelloController@update');
Route::get('hello/del','App\Http\Controllers\HelloController@del');
Route::post('hello/del','App\Http\Controllers\HelloController@remove');
Route::get('upload','App\Http\Controllers\HelloController@upload');
Route::post('upload','App\Http\Controllers\HelloController@upload');








// Route::post('hello/', 'App\Http\Controllers\HelloController@post');
// Route::get('hello', function () {
//     return view('index');
// });
// Route::get('hello', [HelloController::class, 'index']);
// Route::get('hello', 'App\Http\Controllers\HelloController');
// Route::get('hello/other', 'App\Http\Controllers\HelloController@other');
// Route::get('hello/{id?}/{pass?}', 'App\Http\Controllers\HelloController@index');

// Route::get('hello', function () {
//     return '<html><body><h1>Hello</h1><p>This is sample page.</p></body></html>';
// });

// $html = <<<EOR
// <html>
// <head>
// <title>Hello</title>
// <style>
// body {font-size:16pt; color:#999; }
// h1 { font-size:100pt; text-align:right; color:#eee;
//     margin:-40px 0px -50px 0px;}
// </style>
// </head>
// <body>
//     <h1>Hello</h1>
//     <p>This is sample page.</p>
//     <p>これは、サンプルで作ったページ</p>
// </body>
// </html>
// EOR;

// Route::get('hello', function () use ($html){
//     return $html;
// });

// Route::get('hello/{msg}', function ($msg){

// $html = <<<EOR
// <html>
// <head>
// <title>Hello</title>
// <style>
// body {font-size:16pt; color:#999; }
// h1 { font-size:100pt; text-align:right; color:#eee;
//     margin:-40px 0px -50px 0px;}
// </style>
// </head>
// <body>
//     <h1>Hello</h1>
//     <p>{$msg}</p>
//     <p>これは、サンプルで作ったページ</p>
// </body>
// </html>
// EOR;
//     return $html;
// });

// Route::get('hello/{msg?}', function ($msg='no massage.'){

// $html = <<<EOR
// <html>
// <head>
// <title>Hello</title>
// <style>
// body {font-size:16pt; color:#999; }
// h1 { font-size:100pt; text-align:right; color:#eee;
//     margin:-40px 0px -50px 0px;}
// </style>
// </head>
// <body>
//     <h1>Hello</h1>
//     <p>{$msg}</p>
//     <p>これは、サンプルで作ったページ</p>
// </body>
// </html>
// EOR;
//     return $html;
// });
