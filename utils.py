import cv2

def template_matching(img, template):
    img = cv2.imread(img,0)
    img2 = img.copy()
    template = cv2.imread(template,0)
    w, h = template.shape[::-1]
    threshold = 0.9
    found = False

    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    i = 0
    while not found and i<len(methods):
        i += 1
        # Apply template Matching
        res = cv2.matchTemplate(img, template, eval(methods[i]))
        if len(np.where( res >= threshold)[0]) > 0:
            print("found template")
            found = True
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(img,top_left, bottom_right, 255, 2)


            cv2.imwrite("res.png", res)
            cv2.imwrite("img.png", img)