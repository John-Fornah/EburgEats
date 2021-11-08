<?php
$myPDO = new PDO('sqlite:/desktop/eburg-eats/EburgEats/site.db');
function calculate_stars($max, $rating)
{
    $full_stars = floor($rating);
    $half_stars = ceil($rating - $full_stars);
    $gray_stars = $max - ($full_stars + $half_stars);
    return array($full_stars, $half_stars, $gray_stars);
}

function display_star($rating)
{
    $output = "";
    $number_stars = calculate_stars(5, $rating);
    $full = $number_stars[0];
    $half = $number_stars[1];
    $gray = $number_stars[2];

    $output = '<ul class="star-rating d-sm-flex no-pads">';
    if ($gray)
        for ($i = 0; $i < $gray; $i++) {
            $output .= '<li class="star-icon d-inline-block">
                            <i class="fas fa-star"></i>
                        </li>';
        }
    if ($half) {
        $output .= ' <li class="star-icon d-inline-block half">
                            <i class="fas fa-star"></i>
                        </li>';
    }
    if ($full) {
        for ($i = 0; $i < $full; $i++) {
            $output .= '<li class="star-icon d-inline-block full">
                            <i class="fas fa-star"></i>
                        </li>';
        }
    }
    $output = '</ul>';
    return $output;
}

function show_stars($id){
    $current_rating=0;
    $votes=0;
    include_once("db_connect.php");
    $sql="SELECT total_votes, total_value, used_ips FROM $tableName WHERE id = '$id' ";
    $result = $conn->query($sql);
    $number_rows=$result->num_rows;
    if($number_rows>0){
        $numbers = $result->fetch_assoc();

    }
}

show_stars(1);
exit;
?>